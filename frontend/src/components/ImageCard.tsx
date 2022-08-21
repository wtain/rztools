import React from 'react';
import FileDto from '../dto/FileDto';

interface Props {
  image_provider_url: string;
  file: FileDto;
  onHashClicked: () => void
}

function ImageCard(props: Props) {
  return (
    <div>
      <table>
        <tbody>
          <tr>
            <td>
              <img src={props.image_provider_url + "get_image?path=" + props.file.path}
                alt=""
                width="100%" />
            </td>
          </tr>
          <tr>
            <td>{props.file.created}</td>
            <td>{props.file.lastUpdated}</td>
          </tr>
          <tr>
            <td>{props.file.path}</td>
          </tr>
          <tr>
            <td>
              <div onClick={() => props.onHashClicked()}>
                {props.file.hash}
              </div>
            </td>
          </tr>
          <tr>
            <div>
              <table>
                <tbody>
                {
                    props.file.tags.map(tag =>
                      <tr key={tag.name}>
                        <td>{tag.name}</td>
                        <td>{tag.value}</td>
                      </tr>
                    )
                }
                </tbody>
              </table>
            </div>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default ImageCard;