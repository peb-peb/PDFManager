from flet import *
import PyPDF2


def main(page: Page):
  page.title = "Open PDF Manager"

  BG = '0xffe9a178'
  FG = '0xfff6e1C3'
  BUTTON_COLOR = '0xffA84448'

  def shrink(e):
    page2.controls[0].width = 0
    page2.controls[0].scale = transform.Scale(
      0.8,
      alignment=alignment.center_right
    )
    page2.controls[0].border_radius=border_radius.only(
      topLeft=35,
      topRight=0,
      bottomLeft=35,
      bottomRight=0
    )
    page2.update()

  def restore(e):
    page2.controls[0].width = 300
    page2.controls[0].border_radius = 0
    page2.controls[0].scale = transform.Scale(
      1,
      alignment=alignment.center_right
    )
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
              text='MERGE PDFs',
              height=50,
              width=300,
              style=ButtonStyle(
                bgcolor=BUTTON_COLOR,
              ),
              on_click=page.go('/merge'),
            ),
            FilledTonalButton(
              text='ROTATE PDFs',
              height=50,
              width=300,
              style=ButtonStyle(
                bgcolor=BUTTON_COLOR,
              ),
              on_click=None,
            ),
            FilledTonalButton(
              text='MERGE PDFs',
              height=50,
              width=300,
              style=ButtonStyle(
                bgcolor=BUTTON_COLOR,
              ),
              on_click=None,
            ),
            # Container(
            #   height=50, 
            #   width=300, 
            #   bgcolor=BG,
            #   border_radius=20,
            #   content=Column(
            #     controls=[
            #       Text(
            #         value="MERGE",
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

  page1 = Container(
    width=300,
    height=600,
    bgcolor=BG,
    border_radius=35,
    padding=padding.only(left=20,top=20),
    content=Column(
      controls=
      [
        Column(
          alignment='end',
          controls=[
            Container(
              # alignment=alignment.center,
              border_radius=15,
              padding=padding.only(
                top=2,left=8,
              ),
              height=30,
              width=30,
              border=border.all(color='white',width=1),
              on_click=lambda e: restore(e),
              content=Text('<')
            ),
            Text(value='@peb'),
          ]
        ),
      ]
    )
  )
  page2 = Row(
    controls=[
      Container(
        # expand=True,
        width=300,
        height=600,
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
    # expand=True,
    width=300,
    height=600,
    bgcolor=BG,
    content=Stack(
      controls=[
        page1,
        page2,
      ]
    )
  )

  def pick_files_result1(e: FilePickerResultEvent):
    selected_file1.value = (
        ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    )
    path_pdf1.value = e.files[0].path
    selected_file1.update()

  def pick_files_result2(e: FilePickerResultEvent):
    selected_file2.value = (
        ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    )
    path_pdf2.value = e.files[0].path
    selected_file2.update()

  pick_files_dialog1 = FilePicker(on_result=pick_files_result1)
  pick_files_dialog2 = FilePicker(on_result=pick_files_result2)
  selected_file1 = Text()
  selected_file2 = Text()
  path_pdf1 = Text()
  path_pdf2 = Text()

  # def save_file_result(e: FilePickerResultEvent):
  #   save_file_path.value = e.path if e.path else "Cancelled!"
  #   save_file_path.update()

  # save_file_dialog = FilePicker(on_result=save_file_result)
  # save_file_path = Text()

  # page.overlay.extend([pick_files_dialog1, pick_files_dialog2, save_file_dialog])
  page.overlay.extend([pick_files_dialog1, pick_files_dialog2])

  def merge_pdf(e):
    print(path_pdf1.value)
    pdf1 = open(path_pdf1.value, 'rb')
    pdf2 = open(path_pdf2.value, 'rb')

    merger = PyPDF2.PdfWriter()
    merger.append(pdf1)
    merger.append(pdf2)

    output = open("document-output.pdf", "wb")
    merger.write(output)

    merger.close()
    output.close()
    pdf1.close()
    pdf2.close()

  get_file_contents = Container(
    width=300,
    height=600,
    bgcolor=FG,
    padding=padding.only(
      top=20,
      left=20,
      right=20,
      bottom=20,
    ),
    content=Column(
      controls=[
        Row(
          alignment='spaceBetween',
          controls=[
            Container(
              content=Icon(icons.MENU)
            ),
            Text(
              value='MERGE PDFs',
              scale=1.2,
            )
          ]
        ),
        Container(height=50),
        FilledTonalButton(
          text='Pick PDF1',
          icon=icons.UPLOAD_FILE,
          height=50,
          width=300,
          on_click=lambda _:pick_files_dialog1.pick_files(
            allow_multiple=False,
            allowed_extensions=['pdf'],
          ),
        ),
        selected_file1,
        FilledTonalButton(
          text='Pick PDF2',
          icon=icons.UPLOAD_FILE,
          height=50,
          width=300,
          on_click=lambda _:pick_files_dialog2.pick_files(
            allow_multiple=False,
            allowed_extensions=['pdf'],
          ),
        ),
        selected_file2,
        # FilledTonalButton(
        #   text='Save PDF',
        #   icon=icons.SAVE,
        #   height=50,
        #   width=300,
        #   on_click=lambda _:save_file_dialog.save_file(
        #     allowed_extensions=['pdf'],
        #   ),
        # ),
        # save_file_path,
        FilledTonalButton(
          text='MERGE',
          height=50,
          width=300,
          on_click=merge_pdf,
        ),
      ]
    )
  )

  all_pages = {
    '/': View(
      '/',
      [
        container
      ]
    ),
    '/merge': View(
      '/merge',
      [
        get_file_contents,
      ]
    )
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
