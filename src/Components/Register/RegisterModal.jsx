import CloseIcon from "@mui/icons-material/Close";
import { IconButton } from '@mui/material';
import Modal from '@mui/material/Modal';
import * as React from 'react';

export default function RegisterModal({handleClose, open}) {
  const [todos, setTodos] = React.useState([]);

  const handleAddTodo = () => {
    setTodos([...todos, { text: '' }])
  };
  
  const handleTodoChange = (index, event) => {
    const newTodos = [...todos];
    newTodos[index].text = event.target.value;
    setTodos(newTodos);
  };

  const handleModalClose = (event) => {
    event.stopPropagation();
    handleClose();
    setTodos([]);
  }
  
  return (
    <div>
      <Modal
        open={open}
        // onClose={handleModalClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <div class="registerModal">
            <div class="registerModalTitleArea">
                <div class="registerModalTitle">
                  <IconButton onClick={handleModalClose} aria-label="delete">
                    <CloseIcon />
                  </IconButton>
                  目標追加
                </div>
            </div>
            <div class="targetAreaModal">
                <input 
                  type="form" 
                  class="targetContentModal"
                  placeholder="目標"/>
            </div>
            <div class="todoAreaModal">
                <input 
                  type="form" 
                  class="todoContentModal"
                  placeholder="todo1"/>
                <input 
                  type="form" 
                  class="todoContentModal"
                  placeholder="todo2"/>
                <input 
                  type="form" 
                  class="todoContentModal"
                  placeholder="todo3"/>
                {todos.map((todo, index) => (
                  <input key={index} text={todo.text} class={"todoContentModal"} placeholder={"todo" + (index + 4)}
                    handleChange={(event) => handleTodoChange(index, event)} />
                ))}
            </div>
            <div class="addTodoButton" onClick={handleAddTodo}>
                +
            </div>
            <div class="registerButton">
                登録
            </div>
        </div>
      </Modal>
    </div>
  );
}