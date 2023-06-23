import { useState } from 'react'

const ThreadForm = () => {

	const [threadTitle, setThreadTitle] = useState<string>("");
	const [threadBody, setThreadBody] = useState<string>("");

	return (
		<div className="border-gray-300 border-2 my-8 p-2">
			<p className="font-semibold">New Thread</p>
			<p>Subject</p>
			<input value={threadTitle}
				onChange={e => setThreadTitle(e.target.value)}>
			</input>
			<p>Text</p>
			<textarea value={threadBody}
				onChange={e => setThreadBody(e.target.value)}
				className="w-full md:max-w-5xl">
			</textarea><br />
			<button className="bg-blue-800 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded">Submit</button>
		</div>
	)

}

export default ThreadForm;