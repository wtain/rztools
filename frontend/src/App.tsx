import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import './App.css';
import AppRouter from './components/AppRouter/AppRouter';
import NavBar from './components/NavBar/NavBar';
import RemoteImageRepository from './repository/RemoteImageRepository';
import RemoteTasksRepository from './repository/RemoteTasksRepository';
// import ip from "ip"

function App() {

  // console.dir ( ip.address() );

  // const backend_host = process.env.backend_host ?? "localhost";
  // const backend_port = process.env.backend_port ?? 5000;
  // const backend_url = process.env.backend_url ?? `http://${backend_host}:${backend_port}/`;
  const backend_url = process.env.REACT_APP_BACKEND_URL ?? `http://localhost:5000/`;

  const page_size = 200;

  const imageRepository = new RemoteImageRepository(backend_url, page_size);

  const tasksRepository = new RemoteTasksRepository(backend_url);

  return (
    <BrowserRouter>
      <NavBar />
      <AppRouter imageRepository={imageRepository} tasksRepository={tasksRepository} />
    </BrowserRouter>
  );
}

export default App;
