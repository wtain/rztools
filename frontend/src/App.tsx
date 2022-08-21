import React from 'react';
import './App.css';
import ImagePageView from './components/ImagePageView';
import RemoteImageRepository from './components/RemoteImageRepository';


function App() {

  const [hash, setHash] = React.useState<string>();

  const backend_url = process.env.backend_url ?? "http://localhost:5000/";

  const page_size = 200;

  const imageRepository = new RemoteImageRepository(backend_url, page_size);

  return (
    <ImagePageView onHashClicked={(hash: string) => {
        setHash(hash);
      }}
      imageRepository={imageRepository}  />
  );
}

export default App;
