import CloseIcon from "@mui/icons-material/Close";
import { Box, IconButton, Tab } from "@mui/material";
import Modal from "@mui/material/Modal";
import * as React from "react";
import { TabContext, TabList, TabPanel } from "@mui/lab";
import { useState } from "react";

export default function LoginModal({ handleClose, open }) {
  const [tabValue, setTabValue] = useState("1");
  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  return (
    <div>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        {/* <div class="loginModal">
            <div class="loginInfo">
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
        </div> */}
        <div class="loginModal">
          <TabContext value={tabValue}>
            <TabList
              onChange={handleTabChange}
              aria-label="lab API tabs example"
            >
              <Tab label="新規登録" value="1" />
              <Tab label="ログイン" value="2" />
            </TabList>
            <TabPanel class="loginTab" value="1">
                <div class="loginErrorMessage">

                </div>
              <input
                type="form"
                class="newUserRegisterContent"
                placeholder="ユーザー名"
              />
              <input
                type="form"
                class="newUserRegisterContent"
                placeholder="パスワード"
              />
              <input
                type="form"
                class="newUserRegisterContent"
                placeholder="表示名"
              />
              <div class="newUserRegisterButton">登録</div>
            </TabPanel>
            <TabPanel class="loginTab" value="2">
              <input
                type="form"
                class="newUserRegisterContent"
                placeholder="ユーザー名"
              />
              <input
                type="form"
                class="newUserRegisterContent"
                placeholder="パスワード"
              />
              <div class="userLoginButton">ログイン</div>
            </TabPanel>
          </TabContext>
        </div>
      </Modal>
    </div>
  );
}
