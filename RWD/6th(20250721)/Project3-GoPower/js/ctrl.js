	document.addEventListener("DOMContentLoaded",function(){
		document.addEventListener("keydown",function(e){
			const key=e.key.toLowerCase()
			if(e.ctrlKey || e.key ==="u" || e.key === "F12"){
				e.preventDefault()
				showWarning()
				return false
			}
		})
	})

	document.body.addEventListener("contextmenu",function(e){
		e.preventDefault()
		showWarning()
	})

	function showWarning(){
		const modal=new bootstrap.Modal(document.getElementById('warning'))
		modal.show()
		return false
	}