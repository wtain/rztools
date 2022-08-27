import React from 'react';
import TaskDto from '../../dto/TaskDto';
import TasksRepository from "../../repository/TasksRepository";

interface Props {
  tasksRepository: TasksRepository;
}

function TasksPage(props: Props) {

  const [data, setData] = React.useState<TaskDto[]>([]);
  const [tick, setTick] = React.useState<number>(0);

  const refresh_delay = 3000;

  React.useEffect(() => {

    const fetchData = async () => {
      const results = await props.tasksRepository.getTasks();
      setData(results);
    }

    fetchData();

    setTimeout(() => setTick(tick + 1), refresh_delay);
  }, [props.tasksRepository, tick]);


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
              <tr key={result.taskid}>
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
      <button onClick={() => {
          props.tasksRepository.addTask("scan");
      }}>
        Start
      </button>
    </div>
  )
}

export default TasksPage;