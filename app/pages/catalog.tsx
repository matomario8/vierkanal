import Link from 'next/link'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import ThreadForm from '@/components/ThreadForm'
import ThreadBox from '@/components/ThreadBox'
import config from "@/config.json";

import { useState, useEffect } from 'react'

const inter = Inter({ subsets: ['latin'] })

type Thread = {
	id: string
	title: string
	comment: string
}

const Catalog = () => {

	const [response, setResponse] = useState([])
	const [threads, setThreads] = useState<Thread[]>([])

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

	useEffect(() => {
		fetchThreads().then((result) => {

			updateThreads(result)
		})
	}, [])

	const updateThreads = (data: Thread[]) => {
		setThreads(data)
	}



	return (
		<main
			className={`flex min-h-screen flex-col p-24 ${inter.className}`}
		>
			<div className={"self-center"}>
				<Header title="Technology" imgUrl="/assets/bildschirmfoto.png"></Header>
			</div>
			<ThreadForm></ThreadForm>
			<div className="flex flex-row flex-wrap gap-x-2 text-sm">
				{threads.map((thread: Thread) => (
					<ThreadBox id={thread.id} title={thread.title} comment={thread.comment} />
				))}
			</div>

		</main>
	)
}

export default Catalog;