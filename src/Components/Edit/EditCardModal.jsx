import CloseIcon from "@mui/icons-material/Close";
import { IconButton } from '@mui/material';
import Modal from '@mui/material/Modal';
import * as React from 'react';

export default function EditCardModal({handleClose, open}) {
  
  return (
    <div>
      <Modal
        open={open}
        // onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <div class="EditCardModal">
          <div class="EditCardModalTitle">
            <IconButton onClick={handleClose} aria-label="delete">
              <CloseIcon />
            </IconButton>
            目標編集
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
          </div>
          <div class="registerButton">
              登録
          </div>
        </div>
      </Modal>
    </div>
  );
}