from flet import *
import PyPDF2



def main(page: Page):
  page.title = "Open PDF Manager"

  BG = '0xffe9a178'
  FG = '0xfff6e1C3'

  main_page_contents = Container(
    content=Column(
      controls=[
        Row(
          alignment='spaceBetween',
          controls=[
            Container(
              content=Icon(icons.MENU)
            ),
            # REMOVED: for Account (but no requirement for login)
            # Row(
            #   controls=[
            #     Icon(icons.SEARCH)
            #   ]
            # )
          ]
        ),
        Container(
          height=10
        ),
        Text(
          value="Welcome to OpenPDFManager!"
        ),
        
      ]
    )
  )

  page1 = Container()
  page2 = Row(
    controls=[
      Container(
        expand=True,
        bgcolor=FG,
        padding=padding.only(
          top=20,
          left=20,
          right=20,
          bottom=20,
        ),
        content=Column(
          controls=[
            main_page_contents,
          ]
        )
      )
    ]
  )

  container = Container(
    expand=True,
    bgcolor=BG,
    content=Stack(
      controls=[
        page1,
        page2,
      ]
    )
  )

  page.add(container)
    

app(target=main, assets_dir="assets", upload_dir="assets/uploads")

# encrypt single pdf

# decrypt single pdf

# merge two pdf

# split pdf (split into two parts based on page number)

# trim pdf (remove certain parts of pdf permanently)

# rotate pdf (all pages clockwise/anticlockwise)


# screen resolution: 1080x2160
