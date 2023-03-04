from flet import *
import PyPDF2



def main(page: Page):
  page.title = "Open PDF Manager"

  BG = '0xffe9a178'
  FG = '0xfff6e1C3'
  BUTTON_COLOR = '0xffA84448'

  def shrink(e):
    page2.controls[0].width = 120
    page2.update()

  main_page_contents = Container(
    content=Column(
      controls=[
        Row(
          alignment='spaceBetween',
          controls=[
            Container(
              content=Icon(icons.MENU),
              on_click=lambda e: shrink(e),
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
        Text(
          value="FEATURES"
        ),
        Stack(
          controls=[
            FilledTonalButton(
              text='TRIM PDFs',
              height=50,
              width=300,
              style=ButtonStyle(
                bgcolor=BUTTON_COLOR,
              ),
              # on_click=page.go('/trim')
            ),
            # Container(
            #   height=50, 
            #   width=300, 
            #   bgcolor=BG,
            #   border_radius=20,
            #   content=Column(
            #     controls=[
            #       Text(
            #         value="TRIM",
            #         text_align='CENTRE',
            #       )
            #     ]
            #   )
            # ),
          ]
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

  # get_file_contents = Container(
  #   content=Column(
  #     controls=[
  #       Row(
  #         alignment='spaceBetween',
  #         controls=[
  #           Container(
  #             content=Icon(icons.MENU)
  #           ),
  #         ]
  #       ),
  #     ]
  #   )
  # )

  all_pages = {
    '/': View(
      '/',
      [
        container
      ]
    ),
    # '/trim': View(
    #   '/trim',
    #   [
    #     # get_file_contents,
    #   ]
    # )
  }

  def route_change(route):
    page.views.clear()
    page.views.append(
      all_pages[page.route]
    )

  page.add(container)

  page.on_route_change = route_change
  page.go(page.route)
    

app(target=main, assets_dir="assets", upload_dir="assets/uploads")

# encrypt single pdf

# decrypt single pdf

# merge two pdf

# split pdf (split into two parts based on page number)

# trim pdf (remove certain parts of pdf permanently)

# rotate pdf (all pages clockwise/anticlockwise)


# screen resolution: 1080x2160
