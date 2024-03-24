import streamlit as st
import pickle

st.title('Iris Data Prediction')

sepal_length = st.number_input('Enter sep len: ')
sepal_width = st.number_input('Enter sep wid: ')
petal_length = st.number_input('Enter pet len: ')
petal_width = st.number_input('Enter pet wid: ')

a = st.selectbox('Select the operation:', ('Description of data', 'Prediction'))

if st.button('Execute??'):
    if a == 'Description of data':
        st.write('Development in progress!! Will be back soon')
    else:
        with open('model_file.pkl', 'rb') as models:
            fin_model = pickle.load(models)
        datas = [[sepal_length, sepal_width, petal_length, petal_width]]
        predicted = fin_model.predict(datas)
        st.write(f'My model output is : {predicted}')

        st.error('Problem!!!!')

