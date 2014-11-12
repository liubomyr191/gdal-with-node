var ghpages = require('gh-pages');
var path = require('path');

ghpages.publish(path.resolve(__dirname, '../yuidocs'), function(err) {
	if (err) {
		console.error(err);
		process.exit(1);
	} else {
		process.exit(0);
	}
});