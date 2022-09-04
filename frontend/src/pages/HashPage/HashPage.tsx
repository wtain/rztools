import React from 'react';
import { useParams } from 'react-router-dom';
import ImageCard from '../../components/ImageCard';
import FileDto from '../../dto/FileDto';
import ImageRepository from '../../repository/ImageRepository';

interface Props {
  imageRepository: ImageRepository;
}

function HashPage(props: Props) {

  // todo: unify with ImagesPage

  const image_provider_url = process.env.image_provider_url ?? "http://localhost:8000/";

  const { hash } = useParams();

  const [data, setData] = React.useState<FileDto[]>([]);

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await props.imageRepository.getFilesByHash(hash!);
      setData(results);
    }

    fetchData();
  }, [props.imageRepository, hash]);

  return (
    <div>
      {
        data.map(result => 
          <ImageCard image_provider_url={image_provider_url}
            file={result}
            key={result.path}
            onHashClicked={() => 0}/>
        )
      }
    </div>
  )
}

export default HashPage;