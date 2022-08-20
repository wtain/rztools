import React from 'react';
import TagDto from './TagDto';

interface FileDto {
  path: string;
  hash: string;
  created: string;
  lastUpdated: string;
  size: number;
  tags: TagDto[];
}

export default FileDto;