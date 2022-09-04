import React from 'react';
import TaskDto from '../dto/TaskDto';

interface TasksRepository {
  getTasks: () => Promise<TaskDto[]>;

  addTask: (name: string) => Promise<string>;

  markAllRunningAsFailed: () => Promise<string>;
}

export default TasksRepository;