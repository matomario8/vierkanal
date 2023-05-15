import Link from 'next/link'
import { Inter } from 'next/font/google'
import BoardTitle from '@/components/HeaderBoardTitle'
import HeaderArt from '@/components/HeaderArt'
import HeaderBoards from '@/components/HeaderBoards'
import NewThread from '@/components/NewThread'
import ThreadBox from '@/components/ThreadBox'
import config from "@/config.json";

import { useState, useEffect } from 'react'

const inter = Inter({ subsets: ['latin'] })
type Thread = {
    id: string
    title: string
    comment: string
}
export default function Home() {

  

  const [response, setResponse] = useState([])
  const [threads, setThreads] = useState<JSX.Element[]>([])
  //var threads: JSX.Element[] = []

  const fetchThreads = () => fetch(config.FLASK_API.URL + config.FLASK_API.ENDPOINTS.THREADS.GET_ALL)
    .then(res => {
      if (res.status === 200) {
        return res.json()
      }
    })
    .then((result) => {
      setResponse(result)
      return result
    })
  
    useEffect(()=> {
      fetchThreads().then((result)=> {
        
        updateThreads(result)
      })
    }, [])

  const updateThreads = (data: Thread[]) => {
    let tempThreads: JSX.Element[] = []
    data.forEach((element) => {
      console.log(element)
      tempThreads.push(<ThreadBox id={element.id} title={element.title} comment={element.comment}></ThreadBox>)
    })

    setThreads(tempThreads)
  }



  return (
    <main
      className={`flex min-h-screen flex-col p-24 ${inter.className}`}
    >
      
      <HeaderBoards></HeaderBoards>
      <div className={"self-center"}>
        <BoardTitle title="Technology"></BoardTitle>
        <HeaderArt></HeaderArt>
      </div>
      <NewThread></NewThread>

      <div className="flex flex-row flex-wrap gap-x-2 text-sm">
        {threads}
      </div>

    </main>
  )
}