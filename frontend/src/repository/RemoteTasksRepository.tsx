import axios from "axios";
import TaskDto from "../dto/TaskDto";
import TasksRepository from "./TasksRepository";

class RemoteTasksRepository implements TasksRepository {
  constructor(private backend_url: string) {

  }

  async getTasks(): Promise<TaskDto[]> {
    return await axios
      .get<TaskDto[]>(this.backend_url + "tasks")
      .then((response) => response.data);
  }
}

export default RemoteTasksRepository;