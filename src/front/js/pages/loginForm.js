import React, {useContext, useState} from "react";
import { Context } from "../store/appContext";
import { Navigate } from "react-router-dom";

export const LoginForm = () => {
    const {store, actions} = useContext(Context)
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')    

    const sendData = (e) => {
        e.preventDefault()        
    }

    return(
        <div className="container">
            <div className="body m-5 text-center">
                <h1>Login</h1>
                {store.auth === true ? <Navigate to='/demo' />  :
                <div>                   
                    <form onSubmit={sendData}>
                        <div className="mb-3">
                            <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                            onChange={ (e)=> setEmail(e.target.value) }/>                    
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1"
                            onChange={ (e)=> setPassword(e.target.value) }/>
                        </div>               
                        <button type="submit" className="btn btn-primary" onClick={ ()=> actions.login(email, password) }>Submit</button>
                    </form>
                </div>
                 }
                
            </div>
        </div>
    )
}