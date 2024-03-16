import React from 'react'

const CardListTargetCard = ({style}) => {
    return (
        <div class="targetCard cardListTargetCard" style={style}>
            <div class="targetArea">
                <div class="targetTitle">目標</div>
                <div class="targetContent">XXXX</div>
            </div>
            <div class="todoArea">
                <div class="todoTitle">TODO</div>
                <div class="todoContent">YYYY</div>
                <div class="todoContent">YYYY</div>
                <div class="todoContent">YYYY</div>
            </div>
        </div>
    )
}

export default CardListTargetCard