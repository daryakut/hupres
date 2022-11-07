import {getBaseUrl} from "./server";

const axios = require('axios');

const axiosInstance = axios.create({
  baseURL: `${getBaseUrl()}/api`,
  withCredentials: true,
});

export async function getCurrentUser() {
  try {
    const response = await axiosInstance.get('/users/current');
    // Assuming the API returns the user object directly
    console.log('User details:', response.data.user);
    return response.data.user;
  } catch (error) {
    console.error('There was an error fetching the current user:', error);
    // Handle error appropriately
    throw error;
  }
}

export async function logout() {
  try {
    await axiosInstance.get('/users/logout');
    console.log('User logged out successfully.');
    // Perform any additional cleanup or state updates necessary
  } catch (error) {
    console.error('There was an error logging out:', error);
    // Handle error appropriately
    throw error;
  }
}
