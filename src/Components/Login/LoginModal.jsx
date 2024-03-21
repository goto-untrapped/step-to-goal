import CloseIcon from "@mui/icons-material/Close";
import { Box, IconButton, Tab } from "@mui/material";
import Modal from "@mui/material/Modal";
import * as React from "react";
import { TabContext, TabList, TabPanel } from "@mui/lab";
import { useState } from "react";

export default function LoginModal({ handleClose, open }) {
  const API_HOST = 'http://localhost:8000';
  const SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'TRACE']; // RFC7231
  const [csrfFlag, setCsrfFlag] = useState(false);

  const [tabValue, setTabValue] = useState("1");
  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/myapp/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken' : (await fetchCsrfToken()).token,
        "Access-Control-Allow-Origin" : "http://localhost:8000",
        "Access-Control-Allow-Headers" : "Content-Type"
      },
      credentials: 'include',
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    if (response.status === 200) {
      alert("Login successful");
    } else {
      alert(data.message);
    }
  };

  const fetchCsrfToken = async () => {
    try { 
      const response = await fetch(`${API_HOST}/csrf/`, {
        credentials: 'include'
      });
      return response.json();
    }
    catch(e) {
      console.error(e);
    }
  }

  return (
    <div>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
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
              <div class="loginErrorMessage"></div>
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
              <form onSubmit={handleSubmit}>
                <input
                  type="text"
                  class="newUserRegisterContent"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="ユーザー名"
                />
                <input
                  type="password"
                  class="newUserRegisterContent"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="パスワード"
                />
                <button type="submit" class="userLoginButton">
                  ログイン
                </button>
              </form>
            </TabPanel>
          </TabContext>
        </div>
      </Modal>
    </div>
  );
}
