import { useState } from 'react'

const ThreadForm = () => {

	const [threadTitle, setThreadTitle] = useState<string>("");
	const [threadBody, setThreadBody] = useState<string>("");

	return (
		<div className="w-full my-8">
			<h1 className="text-2xl font-semibold mb-4">
				New Thread
			</h1>
			<label 
				className="block w-full"
				htmlFor="subject"
			>
				Subject
			</label>
			<input 
				className="text-gray-900 p-2 mb-4"
				id="subject"
				onChange={e => setThreadTitle(e.target.value)}
				value={threadTitle}
			>
			</input>
			<label 
				className="block w-full"
				htmlFor="comment"
			>	
				Comment
			</label>
			<textarea 
				className="text-gray-900 w-full md:max-w-5xl h-24 p-2 mb-4"
				id="comment"
				onChange={e => setThreadBody(e.target.value)}
				value={threadBody}
			>
			</textarea><br />
			<button className="bg-blue-800 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded">Submit</button>
		</div>
	)

}

export default ThreadForm;