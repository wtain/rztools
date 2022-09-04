import React from 'react';
import FileDto from '../dto/FileDto';

interface ImageRepository {
  getPageCount: () => Promise<number>;
  getFiles: (page_num: number) => Promise<FileDto[]>;
  getFilesByHash: (hash: string) => Promise<FileDto[]>;
}

export default ImageRepository;