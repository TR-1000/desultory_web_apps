import { useState } from 'react';
import UserForm from './UserForm';
import MiddleTier from './MiddleTier';

function App() {
  const [users, setUsers] = useState([]);

  const onUserAdd = (user) => {
    setUsers([...users, user]);
  };

  return (
    <div>
      <UserForm onUserAdd={onUserAdd} />
      <hr />
      <MiddleTier />
    </div>
  );
}

export default App;
