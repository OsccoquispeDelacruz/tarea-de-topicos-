Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> import clastrs
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print data
NameError: name 'data' is not defined

##################################################################

>>> import clusters
>>> blognames,words,data=clusters.readfile('blogdata.txt')
>>> clust=clusters.hcluster(data)
>>> reload(clusters)
<module 'clusters' from 'C:\Users\WilberOscco\Desktop\wilber oscco\Codigo\clusters.pyc'>
>>> clusters.printclust(clust,labels=blognames)
-
  gapingvoid: "cartoons drawn on the back of business cards"
  -
    -
      Schneier on Security
      Instapundit.com
    -
      The Blotter
      -
        -
          MetaFilter
          -
            SpikedHumor
            -
              Captain's Quarters
              -
                Michelle Malkin
                -
                  -
                    NewsBusters.org - Exposing Liberal Media Bias
                    -
                      -
                        Hot Air
                        Crooks and Liars
                      -
                        Power Line
                        Think Progress
                  -
                    Andrew Sullivan | The Daily Dish
                    -
                      Little Green Footballs
                      -
                        Eschaton
                        -
                          Talking Points Memo: by Joshua Micah Marshall
                          Daily Kos
        -
          43 Folders
          -
            TechEBlog
            -
              -
                Mashable!
                Signum sine tinnitu--by Guy Kawasaki
              -
                -
                  -
                    Slashdot
                    -
                      MAKE Magazine
                      Boing Boing
                  -
                    -
                      Oilman
                      -
                        Online Marketing Report
                        -
                          Treehugger
                          -
                            SimpleBits
                            -
                              Cool Hunting
                              -
                                Steve Pavlina's Personal Development Blog
                                -
                                  -
                                    ScienceBlogs : Combined Feed
                                    Pharyngula
                                  -
                                    BuzzMachine
                                    -
                                      Copyblogger
                                      -
                                        -
                                          The Viral Garden
                                          Seth's Blog
                                        -
                                          -
                                            Bloggers Blog: Blogging the Blogsphere
                                            -
                                              Sifry's Alerts
                                              ProBlogger Blog Tips
                                          -
                                            -
                                              Valleywag
                                              Scobleizer - Tech Geek Blogger
                                            -
                                              -
                                                O'Reilly Radar
                                                456 Berea Street
                                              -
                                                Lifehacker
                                                -
                                                  Quick Online Tips
                                                  -
                                                    Publishing 2.0
                                                    -
                                                      Micro Persuasion
                                                      -
                                                        A Consuming Experience (full feed)
                                                        -
                                                          John Battelle's Searchblog
                                                          -
                                                            Search Engine Watch Blog
                                                            -
                                                              Read/WriteWeb
                                                              -
                                                                Official Google Blog
                                                                -
                                                                  Search Engine Roundtable
                                                                  -
                                                                    Google Operating System
                                                                    Google Blogoscoped
                    -
                      -
                        -
                          -
                            Blog Maverick
                            -
                              Download Squad
                              -
                                CoolerHeads Prevail
                                -
                                  Joystiq
                                  The Unofficial Apple Weblog (TUAW)
                          -
                            Autoblog
                            -
                              Engadget
                              TMZ.com
                        -
                          Matt Cutts: Gadgets, Google, and SEO
                          -
                            PaulStamatiou.com
                            -
                              -
                                GigaOM
                                TechCrunch
                              -
                                -
                                  Techdirt
                                  Creating Passionate Users
                                -
                                  Joho the Blog
                                  -
                                    -
                                      PerezHilton.com
                                      Jeremy Zawodny's blog
                                    -
                                      Joi Ito's Web
                                      -
                                        ongoing
                                        -
                                          Joel on Software
                                          -
                                            -
                                              we make money not art
                                              -
                                                plasticbag.org
                                                -
                                                  Signal vs. Noise
                                                  -
                                                    kottke.org
                                                    -
                                                      Neil Gaiman's Journal
                                                      -
                                                        -
                                                          The Huffington Post | Raw Feed
                                                          -
                                                            Wonkette
                                                            -
                                                              Gawker
                                                              -
                                                                The Superficial - Because You're Ugly
                                                                Go Fug Yourself
                                                        -
                                                          Deadspin
                                                          Gothamist
                                            -
                                              Kotaku
                                              Gizmodo
                      -
                        Shoemoney - Skills to pay the bills
                        -
                          flagrantdisregard
                          -
                            WWdN: In Exile
                            -
                              Derek Powazek
                              -
                                lifehack.org
                                Dave Shea's mezzoblue
                -
                  Wired News: Top Stories
                  -
                    Topix.net Weblog
                    Bloglines | News
>>> 
