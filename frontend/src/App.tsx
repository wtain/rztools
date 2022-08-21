import axios from 'axios';
import React from 'react';
// import logo from './logo.svg';
import './App.css';
import PageSwitcher from './components/PageSwitcher';
import FileDto from './dto/FileDto';


function App() {
  // process.env.

  const backend_url = "http://localhost:5000/";
  const image_provider_url = "http://localhost:8000/";

  const page_size = 200;

  const [data, setData] = React.useState<FileDto[]>([]);

  const [page_num, setPageNum] = React.useState<number>(() => 1)
  const [page_count, setPageCount] = React.useState<number>(() => 1)

  React.useEffect(() => {

    const fetchData = async () => {
      const cnt = await axios.get<number>(backend_url + "page_count?size=" + page_size)
        .then((response) => response.data);
        setPageCount(cnt);
    }

    fetchData();
  }, [page_num, page_count]);

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await axios.get<FileDto[]>(backend_url + "page?num=" + page_num + "&size=" + page_size)
        .then((response) => response.data);
      setData(results);
    }

    fetchData();
  }, [page_num, page_count]);

  return (
    <div>
      <PageSwitcher page_num={page_num} page_count={page_count}
        onCurrentPageChanged={(new_page: number) => setPageNum(new_page)} />
      <br />
      {
        data.map(result => 
          <img src={image_provider_url + "get_image?path=" + result.path} key={result.path} />
        )
      }
    </div>
  );
}

export default App;
