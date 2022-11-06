const axios = require('axios');

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
});

export async function createQuiz() {
  try {
    const response = await axiosInstance.post('/quizzes');
    return response.data;
  } catch (error) {
    console.error('There was an error creating the quiz:', error);
    throw error;
  }
}

export async function getQuizzes() {
  try {
    const response = await axiosInstance.get('/quizzes');
    return response.data.quizzes;
  } catch (error) {
    console.error('There was an error fetching the quizzes:', error);
    throw error;
  }
}

export async function deleteQuiz(quizToken) {
  try {
    await axiosInstance.delete(`/quizzes/${quizToken}`);
    console.log('Quiz deleted successfully');
  } catch (error) {
    console.error(`There was an error deleting the quiz with token ${quizToken}:`, error);
    throw error;
  }
}

export async function updateQuiz(quizToken, subjectName, pronounce) {
  try {
    await axiosInstance.post(`/quizzes/${quizToken}`, {
      subject_name: subjectName,
      pronounce: pronounce,
    });
    console.log('Quiz updated successfully');
  } catch (error) {
    console.error(`There was an error updating the quiz with token ${quizToken}:`, error);
    throw error;
  }
}

export async function getNextQuizQuestion(quizToken) {
  try {
    const response = await axiosInstance.post(`/quizzes/${quizToken}/generate-next-question`);
    return response.data;
  } catch (error) {
    console.error(`There was an error getting the next question for quiz token ${quizToken}:`, error);
    throw error;
  }
}

export async function submitQuizAnswer(quizQuestionToken, answerName) {
  try {
    const response = await axiosInstance.post(`/quiz-questions/${quizQuestionToken}/submit-answer`, {
      answer_name: answerName,
    });
    return response.data;
  } catch (error) {
    console.error(`There was an error submitting the answer for question token ${quizQuestionToken}:`, error);
    throw error;
  }
}

export async function generateQuizSummary(quizToken) {
  try {
    const response = await axiosInstance.post(`/quizzes/${quizToken}/generate-summary`);
    return response.data;
  } catch (error) {
    console.error(`There was an error generating the summary for quiz token ${quizToken}:`, error);
    throw error;
  }
}
