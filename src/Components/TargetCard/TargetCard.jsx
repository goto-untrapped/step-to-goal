import React from 'react'

const TargetCard = ({targets}) => {
    return (
        // <div class="targetCard">
        //     <div class="targetArea">
        //         <div class="targetTitle">目標</div>
        //         <div class="targetContent">XXXX</div>
        //     </div>
        //     <div class="todoArea">
        //         <div class="todoTitle">TODO</div>
        //         <div class="todoContent">YYYY</div>
        //         <div class="todoContent">YYYY</div>
        //         <div class="todoContent">YYYY</div>
        //     </div>
        // </div>

        targets.length > 0 &&
        targets.map((target, index) => (
        <div class="targetCard cardListTargetCard">
            <div class="targetArea">
            <div class="targetTitle">目標</div>
            <div key={index} className="targetContent">
                {target.content}
            </div>
            </div>

            <div class="todoArea">
            <div class="todoTitle">TODO</div>
            {target.todos.length > 0 &&
                target.todos.map((todo, index) => (
                <div key={index} class="todoContent">
                    {todo.content}
                </div>
                ))}
            </div>
        </div>
        ))
    )
}

export default TargetCard