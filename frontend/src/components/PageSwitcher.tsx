import React from 'react';
import cl from '../App.module.css'

interface Props {
    page_num: number;
    page_count: number;
    onCurrentPageChanged: (new_page: number) => void;
}

interface State {
    
}

function range(start, end) {
    return Array(end - start + 1)
        .fill(0)
        .map((_, idx) => start + idx);
}

class PageSwitcher extends React.Component<Props, State> {

    render() {
        return (
            <div>
                {
                    range(1, this.props.page_count).map(page_num_it => 
                    <button
                        key={page_num_it}
                        className={this.props.page_num === page_num_it ? cl.page_button_selected : cl.default }
                        onClick={() => this.props.onCurrentPageChanged(page_num_it)}>{page_num_it}</button>
                    )
                }
            </div>
        )
    }
}

export default PageSwitcher;