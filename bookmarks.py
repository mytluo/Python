# only partially complete - how to show on web browser?
import shelve
def main():
	""" displays text menu to save, find, update, delete, or view all bookmarks 
		records user choice and calls on appropriate method needed """
    prompt = """
    (S)ave New Bookmark
    (F)ind Bookmark
    (U)pdate Bookmark
    (D)elete Bookmark
    (V)iew Bookmarks
    (Q)uit

    Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            if choice not in "sfudvq":
                print("Invalid menu option")
            else:
                chosen = True
        if choice == 'f':
            keyword = input("Search word: ")
            find_url(keyword.strip())
        if choice == 's': save_url()
        if choice == 'u': update_url()
        if choice == 'd': delete_url()
        if choice == 'v': view_bookmarks()
        if choice == 'q': done = True
def save_url():
	""" saves URL, site name, and optional site description into a shelve object """
    bookmarks = shelve.open("bookmarks")
    url = input("Enter URL: ")
    site = input("Enter site name: ")
    if not url or not site:
        print("Invalid entry.")
        main()
        return
    desc = input("Enter site description (optional): ")
    if not desc:
         desc = "No description"
    bookmarks[url] = [site, desc]
    bookmarks.close()
def find_url(keyword):
	""" takes keyword and looks for matches in the shelve object dictionary
		prints and returns first match, or return None if no matches found """
    bookmarks = shelve.open("bookmarks")
    for url in bookmarks:
        if keyword in url or keyword in bookmarks[url]:
            print(url, bookmarks[url])
            return url, bookmarks[url]
    print("no match found.")
    bookmarks.close()
    return None
def update_url():
	""" updates URL, site name, or site description of existing entry in shelve object """
    bookmarks = shelve.open("bookmarks", writeback=True)
    bkmk = input("Enter URL or site name to update: ")
    match = list(find_url(bkmk))
    if match:
        url = match[0]
        new_url = input("Enter new URL, or hit Enter to continue: ")
        site_name = input("Enter new site name, or hit Enter to continue: ")
        descrip = input("Enter new description, or hit Enter to continue: ")
        if new_url:
            bookmarks[new_url] = bookmarks.pop(url)
        if site_name:
            bookmarks[url][0] = site_name
        if descrip:
            bookmarks[url][1] = descrip
    bookmarks.close()
def delete_url():
	""" deletes existing key-value entry in shelve object """ 
    bookmarks = shelve.open("bookmarks")
    key = input("Enter URL to delete: ")
    try:
        bookmarks.pop(key)
    except (KeyError, ValueError):
        print("URL not found.")
    bookmarks.close()
def view_bookmarks():
	""" view all key-value entries currently stored in shelve object """
    bookmarks = shelve.open("bookmarks")
    for url in bookmarks:
        print(url, bookmarks[url])
    bookmarks.close()
if __name__ == '__main__':
    main()
