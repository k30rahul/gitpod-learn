from model import Items
import view
def start():
    ans=Items.get_items()
    view.display(ans)
    Items.update(ans)

    view.display(ans)


if __name__=='__main__':
    start()