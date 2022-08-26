import React from 'react';

interface TaskDto {
  taskid: string;
  status: string;
  task: string;
  created_at: string;
  parameters: string[]; 
  message: string; 
  progress: number;  
  updated_at: string;
}

export default TaskDto;