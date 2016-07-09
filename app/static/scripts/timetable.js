function initialize() {
	var timetable = $('#timetable')
	var daysRow = $('#timetable .days-row')
	var timeColumn = $('#timetable .time-column')
	var dayColumns = $('#timetable .day-columns')

	daysRow.empty()
	timeColumn.empty()
	dayColumns.empty()

	var tableWidth = timetable.width()
	var tableHeight = Math.max(tableWidth * 1.5, 700)
	var scrollWidth = getScrollWidth()

	timeColumn.css('height', tableHeight)
	dayColumns.css('height', tableHeight)

	days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
	for(var d = 0; d < 7; d++) {
		var dayLabel = document.createElement('div')
		dayLabel.innerHTML = days[d]
		dayLabel.style.display = 'inline-block'
		dayLabel.style.position = 'absolute'
		dayLabel.style.left = (tableWidth-scrollWidth) / 8 * (d+1)
		dayLabel.style.width = (tableWidth-scrollWidth) / 8 - 2
		dayLabel.style.padding = '5 0px'
		dayLabel.style.margin = '3 1 0 1px'
		// dayLabel.style.borderRadius = '4px'
		dayLabel.style.backgroundColor = '#FF6B6B'
		dayLabel.style.color = '#FFFFFF'
		dayLabel.style.fontSize = 15
		dayLabel.style.textAlign = 'center'
		daysRow.append(dayLabel)

		if(d % 2 == 1) {
			var columnDeco = document.createElement('div')
			columnDeco.style.position = 'absolute'
			columnDeco.style.left = (tableWidth-scrollWidth) / 8 * (d+1)
			columnDeco.style.width = (tableWidth-scrollWidth) / 8
			columnDeco.style.height = tableHeight
			columnDeco.style.backgroundColor = '#FAF0DF'
			dayColumns.append(columnDeco)
		}
	}

	timeColumn.css('backgroundColor', '#FAF0DF')

	for(var t = 0; t < 25; t++) {
		var timeLabel = document.createElement('div')
		timeLabel.innerHTML = ('00' + t).substr(-2) + ':00'
		timeLabel.style.position = 'absolute'
		timeLabel.style.top = tableHeight / 50 * (2*t+1) - 8
		timeLabel.style.width = (tableWidth-scrollWidth) / 8 - 2
		timeLabel.style.color = '#7E7E7E'
		timeLabel.style.fontSize = 15
		timeLabel.style.textAlign = 'center'
		timeColumn.append(timeLabel)

		for(var d = 0; d < 7; d++) {
			var timeScaleLine = document.createElement('div')
			timeScaleLine.style.position = 'absolute'
			timeScaleLine.style.top = tableHeight / 50 * (2*t+1)
			timeScaleLine.style.left = (tableWidth-scrollWidth)	/ 8 * (d+1)
			timeScaleLine.style.width = (tableWidth-scrollWidth) / 8 - 1
			timeScaleLine.style.height = 1
			timeScaleLine.style.padding = 0
			timeScaleLine.style.margin = 0
			timeScaleLine.border = 0
			if(d % 2 == 0) timeScaleLine.style.backgroundColor = '#FAF0DF'
			else timeScaleLine.style.backgroundColor = '#FEFAEC'
			dayColumns.append(timeScaleLine)
		}
	}
}

$(function(){
	initialize()
	$(window).resize(initialize)
})