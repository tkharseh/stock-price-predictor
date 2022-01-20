import React, { useState, useEffect } from 'react'
import logo from './images/search_icon.png'


export default function App() {
  const [data, setData] = useState({})
  const [searchTerm, setSearchTerm] = useState()
  const [submittedTerm, setSubmittedTerm] = useState('AAPL')
  const url = "/data?ticker=" + submittedTerm

  useEffect(() => {
    function fetchData() {
      fetch(url).then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }
    fetchData()
  }, [submittedTerm])


  function submit(e) {
    setSubmittedTerm(searchTerm)
    e.preventDefault()
  }

  return (
    <div>

      <div class="w-screen z-96 py-9 place-content-center shadow-2xl flex items-center justify-center">
        <form class="flex" onSubmit={(e) => submit(e)}>
          <input style={{ width: 900 }} class="border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Enter a stock symbol, e.g. 'AAPL'" type="text" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}></input>
          <div class="pl-9 pr-9">
            <button class="font-bold px-9 w-full border border-gray-300 text-white-900 text-sm rounded-lg w-full p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 bg-black hover:bg-slate-700" onSubmit={submit}> <img class="w-5" src={logo} alt="my image"/> </button>
          </div>
        </form>
      </div>
    </div>
  )
}