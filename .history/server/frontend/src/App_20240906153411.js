import LoginPanel from "./components/Login/Login"
import Register from "./components/Register/Register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
<<<<<<< HEAD
=======
      <Route path="/register" element={<Register />} />
>>>>>>> fb9fc0d (React login/logout)
    </Routes>
  );
}
export default App;
