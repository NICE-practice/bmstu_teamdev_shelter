import { makeAutoObservable } from "mobx";

export default class UserStore {
  constructor() {
    this._isAuth = false;
    this._user = {};
    this._privilege = 0;
    makeAutoObservable(this);
  }

  setIsAuth(bool) {
    this._isAuth = bool;
  }
  setUser(user) {
    this._user = user;
  }

  setPrivilege(privilege) {
    this._privilege = privilege;
  }

  get isAuth() {
    return this._isAuth;
  }
  get user() {
    return this._user;
  }
  get privilege() {
    return this._privilege;
  }
}
