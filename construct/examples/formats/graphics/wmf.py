"""
Windows Meta File
"""

from construct import *


wmf_record = Struct(
    "size" / Int32ul, # size in words, including the size, function and params
    "function" / Enum(Int16ul,
        AbortDoc = 0x0052,
        Aldus_Header = 0x0001,
        AnimatePalette = 0x0436,
        Arc = 0x0817,
        BitBlt = 0x0922,
        Chord = 0x0830,
        CLP_Header16 = 0x0002,
        CLP_Header32 = 0x0003,
        CreateBitmap = 0x06FE,
        CreateBitmapIndirect = 0x02FD,
        CreateBrush = 0x00F8,
        CreateBrushIndirect = 0x02FC,
        CreateFontIndirect = 0x02FB,
        CreatePalette = 0x00F7,
        CreatePatternBrush = 0x01F9,
        CreatePenIndirect = 0x02FA,
        CreateRegion = 0x06FF,
        DeleteObject = 0x01F0,
        DibBitblt = 0x0940,
        DibCreatePatternBrush = 0x0142,
        DibStretchBlt = 0x0B41,
        DrawText = 0x062F,
        Ellipse = 0x0418,
        EndDoc = 0x005E,
        EndPage = 0x0050,
        EOF = 0x0000,
        Escape = 0x0626,
        ExcludeClipRect = 0x0415,
        ExtFloodFill = 0x0548,
        ExtTextOut = 0x0A32,
        FillRegion = 0x0228,
        FloodFill = 0x0419,
        FrameRegion = 0x0429,
        Header = 0x0004,
        IntersectClipRect = 0x0416,
        InvertRegion = 0x012A,
        LineTo = 0x0213,
        MoveTo = 0x0214,
        OffsetClipRgn = 0x0220,
        OffsetViewportOrg = 0x0211,
        OffsetWindowOrg = 0x020F,
        PaintRegion = 0x012B,
        PatBlt = 0x061D,
        Pie = 0x081A,
        Polygon = 0x0324,
        Polyline = 0x0325,
        PolyPolygon = 0x0538,
        RealizePalette = 0x0035,
        Rectangle = 0x041B,
        ResetDC = 0x014C,
        ResizePalette = 0x0139,
        RestoreDC = 0x0127,
        RoundRect = 0x061C,
        SaveDC = 0x001E,
        ScaleViewportExt = 0x0412,
        ScaleWindowExt = 0x0410,
        SelectClipRegion = 0x012C,
        SelectObject = 0x012D,
        SelectPalette = 0x0234,
        SetBKColor = 0x0201,
        SetBKMode = 0x0102,
        SetDibToDev = 0x0D33,
        SelLayout = 0x0149,
        SetMapMode = 0x0103,
        SetMapperFlags = 0x0231,
        SetPalEntries = 0x0037,
        SetPixel = 0x041F,
        SetPolyFillMode = 0x0106,
        SetReLabs = 0x0105,
        SetROP2 = 0x0104,
        SetStretchBltMode = 0x0107,
        SetTextAlign = 0x012E,
        SetTextCharExtra = 0x0108,
        SetTextColor = 0x0209,
        SetTextJustification = 0x020A,
        SetViewportExt = 0x020E,
        SetViewportOrg = 0x020D,
        SetWindowExt = 0x020C,
        SetWindowOrg = 0x020B,
        StartDoc = 0x014D,
        StartPage = 0x004F,
        StretchBlt = 0x0B23,
        StretchDIB = 0x0F43,
        TextOut = 0x0521,
        default = Pass,
    ),
    "params" / Array(this.size - 3, Int16ul),
)

wmf_placeable_header = Struct(
  "key" / Const(Int32ul, 0x9AC6CDD7),
  "handle" / Int16ul,
  "left" / Int16sl,
  "top" / Int16sl,
  "right" / Int16sl,
  "bottom"/ Int16sl,
  "units_per_inch"/ Int16ul,
  Padding(4),
  "checksum" / Int16ul,
)

wmf_file = Struct(
    # --- optional placeable header ---
    "placeable_header" / Optional(wmf_placeable_header),

    # --- header ---
    "type" / Enum(Int16ul, 
        InMemory = 0,
        File = 1,
    ),
    "header_size" / Const(Int16ul, 9),
    "version" / Int16ul,
    "size" / Int32ul, # file size is in words
    "number_of_objects" / Int16ul,
    "size_of_largest_record" / Int32ul,
    "number_of_params" / Int16ul,

    # --- records ---
    "records" / GreedyRange(wmf_record)
)
