import sys, json, urllib, urllib2, random
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import config
	
class GuiGTK:
	def __init__(self):
		self.widgets = gtk.glade.XML('main.glade', 'mainWindow')
		events = { 'on_button1_clicked': self.monclic,
					'delete': self.delete }
		self.widgets.signal_autoconnect(events)
		
	def delete(self, source=None, event=None):
		gtk.main_quit()
	
	def monclic(self, source=None, event=None):
		#self.widgets.get_widget('label1').set_text('test')
		imgur = "https://api.imgur.com/3/gallery/random/random/1"
		req = urllib2.Request(imgur);
		req.add_header('Authorization', config.client_id);
		res = urllib2.urlopen(req);
		data = json.loads(res.read());
		count = 0;
		goodList = [];
		linky = "";
		
		for x in data["data"]:
			if 'type' in x:
				if (x["type"] == 'image/jpeg') or (x["type"] == 'image/png'):
					#print count,x["id"],x["type"],x["link"];
					goodList.append(count)
			count += 1;
		
		rline = random.choice(goodList)
		linky = data["data"][rline]["link"]
		
		fname = linky.split('/')[-1]
		fext = fname.split('.')[-1]
		fnew = 'temp.' + fext
		urllib.urlretrieve(linky, fnew);
		self.widgets.get_widget('label1').set_text(fnew)
		pixbuf = gtk.gdk.pixbuf_new_from_file(fnew);

		maxw = 300
		maxh = 300
		orw = pixbuf.get_width()
		orh = pixbuf.get_height()
		proph = float(orh)/(float(orw)/maxw)
		propw = float(orw)/(float(orh)/maxh)
		
		if proph > maxh:
			tarw = int(propw)
			tarh = int(maxh)
		else:
			tarw = int(maxw)
			tarh = int(proph)
		
		pixbuf = pixbuf.scale_simple(tarw, tarh, gtk.gdk.INTERP_BILINEAR);
				
		self.widgets.get_widget('image1').set_from_pixbuf(pixbuf);
		return True
	
if __name__ == '__main__':
	app = GuiGTK()
	gtk.main()
