import CloseIcon from "@mui/icons-material/Close";
import { IconButton } from "@mui/material";
import Modal from "@mui/material/Modal";
import axios from "axios";
import * as React from "react";
import { useState } from "react";

export default function RegisterModal({ handleClose, open }) {
  const [todos, setTodos] = React.useState(["", "", ""]);
  const API_HOST = "http://localhost:8000";

  const handleAddTodo = () => {
    setTodos([...todos, { text: "" }]);
    // setTodos([...todos, ""]);
  };

  const handleTodoChange = (index, event) => {
    const newTodos = [...todos];
    // newTodos[index].text = event.target.value;
    newTodos[index] = { text: event.target.value };
    setTodos(newTodos);
  };

  const handleModalClose = (event) => {
    event.stopPropagation();
    handleClose();
    setTodos([]);
  };

  const fetchCsrfToken = async () => {
    try {
      const response = await fetch(`${API_HOST}/csrf/`, {
        credentials: "include",
      });
      return response.json();
    } catch (e) {
      console.error(e);
    }
  };

  const [target, setTarget] = useState("");
  const handleSubmit = async () => {
    try {
      const csrfToken = (await fetchCsrfToken()).token;

      const response = await axios.post(
        "/api/save/",
        {
          target: target,
          // todos: JSON.stringify({ todos }),
          todos: todos,
          username: localStorage.getItem('username'),
        },
        {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
            "Access-Control-Allow-Origin": "http://localhost:8000",
            "Access-Control-Allow-Headers": "Content-Type",
          },
          withCredentials: true, // クッキーを含むために必要なオプション
        }
      );

      console.log(response.data);
    } catch (error) {
      console.error("Error saving data:", error);
    }
  };

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
              value={target}
              placeholder="目標"
              onChange={(e) => setTarget(e.target.value)}
            />
          </div>
          <div class="todoAreaModal">
            {todos.map((todo, index) => (
              <input
                key={index}
                text={todo.text}
                value={todo.text}
                class={"todoContentModal"}
                placeholder={"todo" + (index + 1)}
                // handleChange={(event) => handleTodoChange(index, event)}
                onChange={(event) => handleTodoChange(index, event)}
              />
            ))}
          </div>
          <div class="addTodoButton" onClick={handleAddTodo}>
            +
          </div>
          <button class="registerButton" onClick={handleSubmit}>
            登録
          </button>
        </div>
      </Modal>
    </div>
  );
}
