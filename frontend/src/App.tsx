import axios from 'axios';
import React from 'react';
// import logo from './logo.svg';
import './App.css';
import cl from './App.module.css'
import FileDto from './FileDto';

function range(start, end) {
  return Array(end - start + 1).fill(0).map((_, idx) => start + idx)
}

function App() {
  // process.env.

  const page_size = 20;

  const [data, setData] = React.useState<FileDto[]>([]);

  const [page_num, setPageNum] = React.useState<number>(() => 1)
  const [page_count, setPageCount] = React.useState<number>(() => 1)

  React.useEffect(() => {

    const fetchData = async () => {
      const cnt = await axios.get<number>("http://localhost:5000/page_count?size=" + page_size)
        .then((response) => response.data);
        setPageCount(cnt);
    }

    fetchData();
  }, [page_num, page_count]);

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await axios.get<FileDto[]>("http://localhost:5000/page?num=" + page_num + "&size=" + page_size)
        .then((response) => response.data);
      setData(results);
    }

    fetchData();
  }, [page_num, page_count]);


  return (
    <div>
      {
        range(1, page_count).map(page_num_it => 
          <button
            key={page_num_it}
            className={page_num === page_num_it ? cl.page_button_selected : cl.default }
            onClick={() => setPageNum(page_num_it)}>{page_num_it}</button>
          )
      }
      <br />
      {
        data.map(result => 
          <img src={"http://localhost:8000/get_image?path=" + result.path} key={result.path} />
        )
      }
    </div>
  );
}

export default App;
