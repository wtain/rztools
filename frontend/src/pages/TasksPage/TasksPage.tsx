import React from 'react';
import TaskDto from '../../dto/TaskDto';
import TasksRepository from "../../repository/TasksRepository";

interface Props {
  tasksRepository: TasksRepository;
}

function TasksPage(props: Props) {

  const [data, setData] = React.useState<TaskDto[]>([]);

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await props.tasksRepository.getTasks();
      setData(results);
    }

    fetchData();
  }, [props.tasksRepository]);

  // todo: background update
  // todo: addition

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>taskid</th>
            <th>task</th>
            <th>parameters</th>
            <th>progress</th>
            <th>status</th>
            <th>message</th>
            <th>created_at</th>
            <th>updated_at</th>  
          </tr>
        </thead>
        <tbody>
          {
            data.map(result => 
              <tr>
                <td>{ result.taskid }</td>
                <td>{result.task}</td>
                <td>{result.parameters}</td>
                <td>{result.progress}</td>
                <td>{result.status}</td>
                <td>{result.message}</td>
                <td>{result.created_at}</td>
                <td>{ result.updated_at }</td>
              </tr>
            )
          }
        </tbody>
      </table>
    </div>
  )
}

export default TasksPage;