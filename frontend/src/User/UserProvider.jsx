import React, {createContext, useContext, useEffect, useState} from 'react';
import {getCurrentUser} from "../api/users_api";

// Create a context
const UserContext = createContext(null);

// Create a provider component
export const UserProvider = ({children}) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Replace with your AJAX request to fetch user data
    fetchUserData().then(setUser);
  }, []);

  // Fetch user data function (replace with your actual data fetching logic)
  async function fetchUserData() {
    const user = await getCurrentUser()
    console.log("Current user", user);
    return user
  }

  return (
    <UserContext.Provider value={{user, setUser}}>
      {children}
    </UserContext.Provider>
  );
};

// Hook to use the user context
export const useUser = () => useContext(UserContext);
