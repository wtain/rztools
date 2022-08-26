import React from 'react';
import TaskDto from '../dto/TaskDto';

interface TasksRepository {
  getTasks: () => Promise<TaskDto[]>;
}

export default TasksRepository;