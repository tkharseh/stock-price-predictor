import React, { useState, useEffect } from 'react';
import icon from './images/search_icon.png';
import illustration from './images/illustration.svg';
import logo from './images/logo.svg';

export default function App() {
  const [data, setData] = useState({});
  const [searchTerm, setSearchTerm] = useState();
  const [submittedTerm, setSubmittedTerm] = useState('AAPL');
  const url = '/data?ticker=' + submittedTerm;
  useEffect(() => {
    function fetchData() {
      fetch(url)
        .then((res) => res.json())
        .then((data) => {
          setData(data);
          console.log(data);
        });
    }
    fetchData();
  }, [submittedTerm]);

  function submit(e) {
    setSubmittedTerm(searchTerm);
    e.preventDefault();
  }

  return (
    <div>
      <div class="w-screen z-96 py-9 place-content-center shadow-2xl flex items-center justify-center">
        <img class="w-24" src={logo}></img>
        <form class="pl-36 flex" onSubmit={(e) => submit(e)}>
          <input
            style={{ width: 1200 }}
            class="border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Enter a stock symbol, e.g. 'AAPL'"
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          ></input>
          <div class="pl-36">
            <button
              class="font-bold px-9 w-full border border-gray-300 text-white-900 text-sm rounded-lg w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 bg-black hover:bg-slate-700"
              onSubmit={submit}
            >
              {' '}
              <img class="w-5" src={icon} alt="my image" />{' '}
            </button>
          </div>
        </form>
      </div>
      <div class="flex items-center justify-center pt-9">
        <p class="font-bold text-5xl pt-9">
          {typeof data.prediction === 'undefined' ? (
            <p>Enter a stock!</p>
          ) : (
            <p>
              {submittedTerm} will reach a price of ${data.prediction} by
              tomorrow!
            </p>
          )}
        </p>
      </div>

      <div class="grid grid-cols-2">
        <div class="grid grid-rows-1 pl-12">
          <img class="pt-36" style={{ width: 500 }} src={illustration}></img>

          <div>
            <p class="font-bold text-5xl pt-9">Welcome to Neat!</p>
            <p class="pt-4 pr-16">
              Ever wondered what price your favourite stock will reach in the
              near future? Type in a stock ticker in the search bar above and
              find out! Neat uses a long short-term memory (LSTM) neural network
              to predict future stock prices.
            </p>
          </div>
        </div>

        <div class="pt-28">
          <p class="font-bold text-5xl pt-9">About the team:</p>
          <p class="font-bold text-2xl pt-4">Nitin Mahtani</p>
          <p class="pt-4 pr-16">
            3rd year student from Barbados with a major in Computer Science and
            a minor in Statistics and Mathematics. Interested in machine
            learning and AI. Ready to pay off student loans with this project!{' '}
          </p>
          <p class="font-bold text-2xl pt-4">Eric Pimentel Aguiar</p>
          <p class="pt-4 pr-16">
            3rd year Computer Science specialist interested in learning AI and
            making $$. A natural bookworm, does not want to sell textbooks to
            pay rent. Need $$. Expects 1000% payoff on the next month! 🤑{' '}
          </p>
          <p class="font-bold text-2xl pt-4">Amiel Nurja</p>
          <p class="pt-4 pr-16">
            2nd year student from Toronto doing a specialist in Computer
            Science, majoring in Mathematics and minoring in Statistics.
            Interested in software engineering and data science. Securing the 💰
            with these NEAT returns! 📈📈{' '}
          </p>
          <p class="font-bold text-2xl pt-4">Tariq Kharseh</p>
          <p class="pt-4 pr-16">
            3rd year student majoring in Cognitive Science with minors in
            Computer Science and Mathematics. This AI stuff is pretty cool,
            can't wait to make massive gains! 💪💰{' '}
          </p>
        </div>
      </div>
    </div>
  );
}
