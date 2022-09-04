import React from 'react';
import FileDto from '../dto/FileDto';
import ImageCard from './ImageCard';
import ImageRepository from '../repository/ImageRepository';
import PageSwitcher from './PageSwitcher';


interface Props {
  onHashClicked: (hash: string) => void
  imageRepository: ImageRepository;
}

function ImagePageView(props: Props) {

  // todo: to properties (same in hashpage)
  // todo: rename to page and move to pages
  const image_provider_url = process.env.REACT_APP_IMAGE_PROVIDER_URL ?? "http://localhost:8000/";

  const [data, setData] = React.useState<FileDto[]>([]);

  const [page_num, setPageNum] = React.useState<number>(() => 1)
  const [page_count, setPageCount] = React.useState<number>(() => 1)

  React.useEffect(() => {

    const fetchData = async () => {
      const cnt = await props.imageRepository.getPageCount();
      setPageCount(cnt);
    }

    fetchData();
  }, [props.imageRepository, page_num]);

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await props.imageRepository.getFiles(page_num);
      setData(results);
    }

    fetchData();
  }, [props.imageRepository, page_num]);

  console.log(process.env);

  return (
    <div>
      <PageSwitcher page_num={page_num}
        page_count={page_count}
        onCurrentPageChanged={(new_page: number) => setPageNum(new_page)} />
      <br />
      {
        // process.env!.map(
        //   (key) => `${key} = ${process.env[key]}`
        // )
      }
      {/* <div>REACT_APP_IMAGE_PROVIDER_URL = {process.env.REACT_APP_IMAGE_PROVIDER_URL }</div>
      <div>REACT_APP_BACKEND_URL = {process.env.REACT_APP_BACKEND_URL }</div> */}
      {
        data.map(result => 
          <ImageCard image_provider_url={image_provider_url}
            file={result}
            key={result.path}
            onHashClicked={() => props.onHashClicked(result.hash)}/>
        )
      }
    </div>
  )
}

export default ImagePageView;