import {getBaseUrl} from "./server";

const axios = require('axios');

const axiosInstance = axios.create({
  baseURL: `${getBaseUrl()}/api`,
  withCredentials: true,
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

export async function getQuiz(quizToken) {
  try {
    const response = await axiosInstance.get(`/quizzes/${quizToken}`);
    return response.data.quiz;
  } catch (error) {
    console.error(`There was an error fetching the quiz ${quizToken}:`, error);
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
    const response = await axiosInstance.post(
      `/quizzes/${quizToken}/generate-next-question`, {}, {
        withCredentials: true,
      }
    );
    return response.data;
  } catch (error) {
    console.error(`There was an error getting the next question for quiz token ${quizToken}:`, error);
    throw error;
  }
}

export async function submitQuizAnswer(quizQuestionToken, answerNames) {
  try {
    const response = await axiosInstance.post(`/quiz-questions/${quizQuestionToken}/submit-answer`, {
      answer_names: answerNames,
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

export async function askFreeFormQuestion(quizToken, freeFormQuestion) {
  try {
    const response = await axiosInstance.post(
      `/quizzes/${quizToken}/free-form-questions/ask`,
      {
        free_form_question: freeFormQuestion,
      }
    );
    return response.data.free_form_answer;
  } catch (error) {
    console.error(`There was an error generating the free form question for quiz token ${quizToken}:`, error);
    throw error;
  }
}

export async function getFreeFormQuestions(quizToken) {
  try {
    const response = await axiosInstance.get(
      `/quizzes/${quizToken}/free-form-questions`,
    );
    return response.data.questions;
  } catch (error) {
    console.error(`There was an error getting the free form questions for quiz token ${quizToken}:`, error);
    throw error;
  }
}
