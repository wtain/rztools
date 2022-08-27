import React from 'react';
import cl from './PageSwitcher.module.css'
import RangeHelpers from '../utils/RangeHelpers';

interface Props {
    page_num: number;
    page_count: number;
    onCurrentPageChanged: (new_page: number) => void;
}


function PageSwitcher(props: Props) {
    return (
        <div className={cl.page_switcher}>
            {
                RangeHelpers.range(1, props.page_count)
                    .map(page_num_it => 
                        <button
                            key={page_num_it}
                            className={props.page_num === page_num_it ? cl.page_button_selected : cl.default }
                            onClick={() => props.onCurrentPageChanged(page_num_it)}>
                            {page_num_it}
                        </button>
                    )
            }
        </div>
    )
}

export default PageSwitcher;