
import React from "react";
import { Navigate, Routes } from "react-router-dom";
import { Route } from "react-router-dom";
import ImagePageView from "../ImagePageView";
import ImageRepository from "../../repository/ImageRepository";
import TasksPage from "../../pages/TasksPage/TasksPage";
import TasksRepository from "../../repository/TasksRepository";

interface Props {
  imageRepository: ImageRepository;
  tasksRepository: TasksRepository;
}

const AppRouter = (props: Props) => {

    // todo: Wrap into page class
    const [hash, setHash] = React.useState<string>();
  
  // {/* <Route path="/images/:id" element={<BookmarksPage bookmarksRepository={bookmarksRepository} />} />
  //           <Route path="/tags" element={<TagsPage tagsRepository={tagsRepository} />} /> */}
  //           <Route path="/" element={<Navigate to="/images" />} />

    return (
        <Routes>
          <Route path="/images" element={<ImagePageView onHashClicked={(hash: string) => {
                                                                          setHash(hash);
                                                                        }}
          imageRepository={props.imageRepository} />} />
          <Route path="/tasks" element={<TasksPage tasksRepository={props.tasksRepository} />} />
          <Route path="/" element={<Navigate to="/images" />} />
        </Routes>
    )
}

export default AppRouter;