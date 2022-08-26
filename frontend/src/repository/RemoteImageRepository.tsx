import React from 'react';
import axios from 'axios';
import FileDto from '../dto/FileDto';
import ImageRepository from './ImageRepository';

class RemoteImageRepository implements ImageRepository {

  constructor(private backend_url: string, private page_size: number) {

  }

  async getPageCount(): Promise<number> {
    return await axios
      .get<number>(this.backend_url + "page_count?size=" + this.page_size)
      .then((response) => response.data);
  }

  async getFiles(page_num: number): Promise<FileDto[]> {
    return await axios
      .get<FileDto[]>(this.backend_url + "page?num=" + page_num + "&size=" + this.page_size)
      .then((response) => response.data);
  }
}

export default RemoteImageRepository;