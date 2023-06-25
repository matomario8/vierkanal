import Image from 'next/image'
import React from "react";

type Thread = {
	id: string
	title: string
	comment: string
}

const ThreadBox = (props: Thread) => {

	const { id, title, comment } = props;

	return (<div className="flex flex-col m-4">
		<span>{id}</span>
		<Image 
			alt="post-image" 
			className="w-100 h-100" 
			src="https://picsum.photos/100/100" 
			width="100" 
			height="100" 
		/>
		<span className="font-semibold">{title}</span>
		<span>{comment}</span>
	</div>)
}

export default ThreadBox;