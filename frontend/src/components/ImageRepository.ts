import React from 'react';
import FileDto from '../dto/FileDto';

interface ImageRepository {
  getPageCount: () => Promise<number>;
  getFiles: (page_num: number) => Promise<FileDto[]>;
}

export default ImageRepository;