import streamlit as st
import pandas as pd


st.title("CSV Data Visualizer")
st.header("📲 Upload your data")

csv_file = st.file_uploader(label="Upload your file here", type="csv")

if csv_file is not None:
    # Data visualization code starts here
    st.header("👀 View your data")

    df = pd.read_csv(csv_file)
    df_name = csv_file.name


    # Create toggle button for dataframe view
    if "show_df" not in st.session_state:
        st.session_state.show_df = True

    if st.button("Toggle View"):
        st.session_state.show_df = not st.session_state.show_df

    if st.session_state.show_df:

        st.dataframe(df)

    else:
        st.info("Dataframe view is disabled. Click the button to enable it.")



    # Create dropdown menus and organize them into columns
    column_names = df.columns.tolist()
    col_names_none = column_names.copy()
    col_names_none.insert(0, "None")

    col1, col2, col3 = st.columns(3)
    with col1:
        x_column = st.selectbox(label="Choose your X-Column", options=column_names)

    with col2:
        y_column = st.selectbox(label="Choose your Y-Column", options=column_names)

    with col3:
        hue = st.selectbox(label="Choose your hue (optional)", options=col_names_none)


    # Let user choose chart type
    chart_type = st.selectbox(label="Choose graph type", options=["Scatter", "Line", "Bar"])
    if hue != "None":
        if chart_type == "Scatter":
            st.scatter_chart(df, x=x_column, y=y_column, color=hue)
        elif chart_type == "Line":
            st.line_chart(df, x=x_column, y=y_column, color=hue)
        else:
            st.bar_chart(df, x=x_column, y=y_column, color=hue)
    else:
        if chart_type == "Scatter":
            st.scatter_chart(df, x=x_column, y=y_column)
        elif chart_type == "Line":
            st.line_chart(df, x=x_column, y=y_column)
        else:
            st.bar_chart(df, x=x_column, y=y_column)

